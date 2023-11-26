import fastapi

from spa_page import spapage as ui_spa_page
from typing import Callable, Union



from nicegui import ui


class SPAAPIRouterFrame(ui.element, component='router_frame.js'):
    pass




class SPAAPIRouter(fastapi.APIRouter):

    def spapage(self,
             path: str, *,
             response_timeout: float = 3.0,
             **kwargs,
             ) -> Callable:

        return ui_spa_page(
            path,
            response_timeout=response_timeout,
            api_router=self,
            **kwargs
        )


    # def open(self, target: Union[Callable, str]) -> None:
    #     if isinstance(target, str):
    #         path = target
    #         builder = self.routes[target]
    #     else:
    #         path = {v: k for k, v in self.routes.items()}[target]
    #         builder = target

    #     async def build() -> None:
    #         with self.content:
    #             await ui.run_javascript(f'''
    #                 if (window.location.pathname !== "{path}") {{
    #                     history.pushState({{page: "{path}"}}, "", "{path}");
    #                 }}
    #             ''', respond=False)
    #             result = builder()
    #             if isinstance(result, Awaitable):
    #                 await result
    #     self.content.clear()
    #     background_tasks.create(build())


    def frame(self) -> ui.element:
        self.content = SPAAPIRouterFrame()  # .on('open', lambda e: self.open(e.args))
        return self.content