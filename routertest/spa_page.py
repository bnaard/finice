# from __future__ import annotations

# import asyncio
# import inspect
# import time
# from pathlib import Path
# from typing import TYPE_CHECKING, Any, Callable, Optional, Union

# from fastapi import Request, Response

# from . import background_tasks, binding, core, helpers
# from .client import Client
# from .favicon import create_favicon_route
# from .language import Language


from fastapi import APIRouter, Response, Request
from nicegui import app, ui

from typing import Optional, Any, Callable, Union, Awaitable
import inspect



class spapage:

    def __init__(self,
                 path: str, *,
                 response_timeout: float = 3.0,
                 api_router: Optional[APIRouter] = None,
                 **kwargs: Any,
                 ) -> None:

        self._path = path
        self.response_timeout = response_timeout
        self.kwargs = kwargs
        self.api_router = api_router


    @property
    def path(self) -> str:
        """The path of the page including the APIRouter's prefix."""
        return self.api_router.prefix + self._path


    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        app.remove_route(self.path)  # NOTE make sure only the latest route definition is used
        parameters_of_decorated_func = list(inspect.signature(func).parameters.keys())

        async def decorated(*dec_args, **dec_kwargs) -> Response:
            request = dec_kwargs['request']
            # NOTE cleaning up the keyword args so the signature is consistent with "func" again
            dec_kwargs = {k: v for k, v in dec_kwargs.items() if k in parameters_of_decorated_func}
            with self.api_router.content:
                await ui.run_javascript(f'''
                    if (window.location.pathname !== "{self.path}") {{
                        history.pushState({{page: "{self.path}"}}, "", "{self.path}");
                    }}
                ''', respond=False)
                result = func
                if isinstance(result, Awaitable):
                    await result
            self.api_router.content.clear()
            # background_tasks.create(build())

            # with Client(self) as client:
            #     if any(p.name == 'client' for p in inspect.signature(func).parameters.values()):
            #         dec_kwargs['client'] = client
            #     result = func(*dec_args, **dec_kwargs)
            # if helpers.is_coroutine_function(func):
            #     async def wait_for_result() -> None:
            #         with client:
            #             return await result
            #     task = background_tasks.create(wait_for_result())
            #     deadline = time.time() + self.response_timeout
            #     while task and not client.is_waiting_for_connection and not task.done():
            #         if time.time() > deadline:
            #             raise TimeoutError(f'Response not ready after {self.response_timeout} seconds')
            #         await asyncio.sleep(0.1)
            #     result = task.result() if task.done() else None
            # if isinstance(result, Response):  # NOTE if setup returns a response, we don't need to render the page
            #     return result
            # binding._refresh_step()  # pylint: disable=protected-access
            # return client.build_response(request)

        parameters = [p for p in inspect.signature(func).parameters.values() if p.name != 'client']
        # NOTE adding request as a parameter so we can pass it to the client in the decorated function
        if 'request' not in {p.name for p in parameters}:
            request = inspect.Parameter('request', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=Request)
            parameters.insert(0, request)
        decorated.__signature__ = inspect.Signature(parameters)  # type: ignore

        if 'include_in_schema' not in self.kwargs:
            self.kwargs['include_in_schema'] = True # globals.endpoint_documentation in {'page', 'all'}  # FIXME app.config.endpoint_documentation in {'page', 'all'}

        self.api_router.get(self._path, **self.kwargs)(decorated)
        # Client.page_routes[func] = self.path
        return func



