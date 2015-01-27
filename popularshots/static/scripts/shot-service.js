(function (angular) {
    'use strict';


    var app = angular.module('ShotService', [], function ($httpProvider) {
        $httpProvider.interceptors.push('AuthInterceptor');
        $httpProvider.defaults.headers.common = {};
        $httpProvider.defaults.headers.post = {};
        $httpProvider.defaults.headers.put = {};
        $httpProvider.defaults.headers.patch = {};
    });

    app.service('shotService', ['$http',

        function ($http) {

            var BASE_URL = 'https://api.dribbble.com/v1';
            
            this.listPopular = function (page, success, error) {
                $http.get(BASE_URL + '/shots/?page=' + page).success(success).error(error);
            };

            this.listFavorites = function (success, error) {
                $http.get('/shot/favorites/list').success(success).error(error);
            }; 

            this.addToFavorites = function (data, success, error) {
                $http.post('/shot/favorites/add', data).success(success).error(error);
            }; 

            this.removeFromFavorites = function (id, success, error) {
                $http.delete('/shot/favorites/remove/' + id).success(success).error(error);
            };            
        }
    ]);

    app.factory('AuthInterceptor', function () {
        return {
            request: function (config) {
                var token = '2dc2be1047838f60217de89cae3d25ce348f20f5418e3db9d73214f18e49ff14';
                config.headers = config.headers || {};
                config.headers.Authorization = 'Bearer ' + token;
                return config;
            }
        }
    });


})(angular);
