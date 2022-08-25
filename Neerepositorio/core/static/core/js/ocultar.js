
(self.webpackChunkorion = self.webpackChunkorion || []).push([[773], {
    8393: (__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{
        "use strict";
        __webpack_require__.d(__webpack_exports__, {
            Z: ()=>__WEBPACK_DEFAULT_EXPORT__
        });
        var _ckeditor_ckeditor5_build_classic_build_translations_es__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(2155)
          , _ckeditor_ckeditor5_build_classic_build_translations_es__WEBPACK_IMPORTED_MODULE_0___default = __webpack_require__.n(_ckeditor_ckeditor5_build_classic_build_translations_es__WEBPACK_IMPORTED_MODULE_0__)
          , _ckeditor_ckeditor5_vue2__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(1272)
          , _ckeditor_ckeditor5_vue2__WEBPACK_IMPORTED_MODULE_1___default = __webpack_require__.n(_ckeditor_ckeditor5_vue2__WEBPACK_IMPORTED_MODULE_1__)
          , _ckeditor_ckeditor5_build_classic__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(5234)
          , _ckeditor_ckeditor5_build_classic__WEBPACK_IMPORTED_MODULE_2___default = __webpack_require__.n(_ckeditor_ckeditor5_build_classic__WEBPACK_IMPORTED_MODULE_2__);
        function _slicedToArray(e, t) {
            return _arrayWithHoles(e) || _iterableToArrayLimit(e, t) || _unsupportedIterableToArray(e, t) || _nonIterableRest()
        }
    }
}


430: (e,t,a)=>{
    "use strict";
    a.d(t, {
        Z: ()=>n
    });
    var r = a(7897)
      , o = a.n(r)
      , i = a(1519)
      , s = a.n(i)()(o());
    s.push([e.id, ".fade-enter[data-v-1f22f6d0],.fade-leave-to[data-v-1f22f6d0]{opacity:0}.fade-enter-active[data-v-1f22f6d0],.fade-leave-active[data-v-1f22f6d0],.fade-move[data-v-1f22f6d0]{transition:all .5s}", "", {
        version: 3,
        sources: ["webpack://./resources/js/components/alerta.vue"],
        names: [],
        mappings: "AAuIA,6DACA,SACA,CAEA,oGAGA,kBACA",
        sourcesContent: ['<template>\n  <div style="position: fixed; right: 20px; z-index: 1050;" :style="{top: `${top}px`}">\n    <transition-group name="fade">\n      <div\n        v-for="mensaje in mensajes"\n        :key="mensaje.id"\n        :class="\'alert alert-\' + mensaje.tipo"\n        v-show="mensaje.visible"\n        role="alert"\n        @click="ocultarAlerta(mensaje)"\n        style="position: sticky; max-width: 700px; max-height: 300px; margin-bottom: 7px; padding:13px;">\n        <i id="icono" style="font-size: 1.85em" :class="claseTipo(mensaje)"></i>\n        <div>\n          <div\n            style="padding-top: 2px"\n            :style="estiloMensaje(mensaje)"\n            v-show="mensaje.mensaje"\n            v-html="mensaje.mensaje"></div>\n          <ul style="padding-left: 17px" v-if="mensaje.lista.length>0">\n            <li v-for="item in mensaje.lista" v-html="item"></li>\n          </ul>\n        </div>\n      </div>\n    </transition-group>\n  </div>\n</template>\n\n<script>\n  export default {\n    props: {\n      top: {type: Number, default: 60},\n      timeout: {type: Number, default: 10000},\n    },\n    data() {\n      return {\n        mensajes: [],\n      }\n    },\n    methods: {\n      mostrarAlerta(tipo, mensaje, lista = []) {\n        if (mensaje instanceof Array) {\n          if (mensaje.length === 1) {\n            mensaje = mensaje[0];\n          } else {\n            lista = mensaje;\n            mensaje = null;\n          }\n        }\n\n        if (lista.length === 1) {\n          lista = lista[0];\n        }\n\n        if (mensaje instanceof Object) {\n          lista = mensaje;\n          mensaje = null;\n        }\n        \n        const objetoMensaje = this.crearMensaje(tipo, mensaje, lista);\n        this.mensajes.unshift(objetoMensaje);\n      },\n      crearMensaje(tipo, texto, lista) {\n        const id = this.mensajes.length > 0 ? this.mensajes[0].id : 0;\n        const mensaje = {\n          id: id + 1,\n          tipo: tipo,\n          mensaje: texto,\n          visible: true,\n          lista: [],\n        };\n\n        if (lista instanceof Array) {\n          mensaje.lista = lista;\n        } else if (lista instanceof Object) {\n          mensaje.lista = Object.values(lista).map(item => item[0]);\n        } else {\n          mensaje.lista = [lista];\n        }\n\n        setTimeout(() => this.ocultarAlerta(mensaje), this.timeout);\n\n        return mensaje;\n      },\n      ocultarAlerta(mensaje) {\n        mensaje.visible = false;\n\n        const indice = this.mensajes.indexOf(mensaje);\n\n        if (indice > -1) {\n          this.mensajes.splice(indice, 1);\n        }\n      },\n      ocultarAlertas() {\n        this.mensajes.forEach(mensaje => mensaje.visible = false);\n      },\n      estiloMensaje(mensaje) {\n        if (!_.isEmpty(mensaje.lista)) {\n          return \'font-weight: 500\';\n        }\n        return \'\';\n      },\n      claseTipo(mensaje) {\n        return {\n          \'fas fa-check-circle\': mensaje.tipo === \'success\',\n          \'fas fa-info-circle\': mensaje.tipo === \'info\',\n          \'fas fa-exclamation-circle\': mensaje.tipo === \'warning\',\n          \'fas fa-times-circle\': mensaje.tipo === \'danger\',\n        };\n      }\n\n    },\n  }\n<\/script>\n\n<style scoped>\n  .fade-enter {\n    opacity: 0;\n  }\n\n  .fade-leave-to {\n    opacity: 0;\n  }\n\n  .fade-move,\n  .fade-enter-active,\n  .fade-leave-active {\n    transition: all 0.5s;\n  }\n\n</style>\n'],
        sourceRoot: ""
    }]);
    const n = s
}