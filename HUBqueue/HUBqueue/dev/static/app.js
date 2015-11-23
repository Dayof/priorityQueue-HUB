(function(){
    'use strict';
    angular.module('mainApp',[
        'ngRoute', 
        'ngAnimate', 
        'ngSanitize', 
        'ui.bootstrap',
        'ngCookies'
    ], function($interpolateProvides){
        $interpolateProvides.startSymbol('{[{');
        $interpolateProvides.endSymbol('}]}');
    })
    .run(function run($http, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    });
})();