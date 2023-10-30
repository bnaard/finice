"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.createEditor = void 0;
var rete_1 = require("rete");
var rete_area_plugin_1 = require("rete-area-plugin");
var rete_connection_plugin_1 = require("rete-connection-plugin");
var rete_vue_plugin_1 = require("rete-vue-plugin");
function createEditor(container) {
    return __awaiter(this, void 0, void 0, function () {
        var socket, editor, area, connection, render, a, b;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    socket = new rete_1.ClassicPreset.Socket("socket");
                    editor = new rete_1.NodeEditor();
                    area = new rete_area_plugin_1.AreaPlugin(container);
                    connection = new rete_connection_plugin_1.ConnectionPlugin();
                    render = new rete_vue_plugin_1.VuePlugin();
                    rete_area_plugin_1.AreaExtensions.selectableNodes(area, rete_area_plugin_1.AreaExtensions.selector(), {
                        accumulating: rete_area_plugin_1.AreaExtensions.accumulateOnCtrl()
                    });
                    render.addPreset(rete_vue_plugin_1.Presets.classic.setup());
                    connection.addPreset(rete_connection_plugin_1.Presets.classic.setup());
                    editor.use(area);
                    area.use(connection);
                    area.use(render);
                    rete_area_plugin_1.AreaExtensions.simpleNodesOrder(area);
                    a = new rete_1.ClassicPreset.Node("A");
                    a.addControl("a", new rete_1.ClassicPreset.InputControl("text", { initial: "hello" }));
                    a.addOutput("a", new rete_1.ClassicPreset.Output(socket));
                    return [4 /*yield*/, editor.addNode(a)];
                case 1:
                    _a.sent();
                    b = new rete_1.ClassicPreset.Node("B");
                    b.addControl("b", new rete_1.ClassicPreset.InputControl("text", { initial: "hello" }));
                    b.addInput("b", new rete_1.ClassicPreset.Input(socket));
                    return [4 /*yield*/, editor.addNode(b)];
                case 2:
                    _a.sent();
                    return [4 /*yield*/, area.translate(b.id, { x: 320, y: 0 })];
                case 3:
                    _a.sent();
                    return [4 /*yield*/, editor.addConnection(new rete_1.ClassicPreset.Connection(a, "a", b, "b"))];
                case 4:
                    _a.sent();
                    rete_area_plugin_1.AreaExtensions.zoomAt(area, editor.getNodes());
                    return [2 /*return*/, function () { return area.destroy(); }];
            }
        });
    });
}
exports.createEditor = createEditor;
