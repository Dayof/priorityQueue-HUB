(function(){
    'use strict';
    angular.module('mainApp',[
        'ngRoute', 
        'ngAnimate', 
        'ngSanitize', 
        'ui.bootstrap',
        'ngCookies',
        'ui.calendar'
    ], function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })
    .run(function run($http, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    });
})();