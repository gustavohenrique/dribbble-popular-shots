(function (angular) {
    'use strict';

    var app = angular.module('ShotController', ['ShotService']);

    app.controller('ShotCtrl', ['$scope', 'shotService',

        function ($scope, shotService) {

            var handleError = function (res) {
                console.log('error', res);
            };
            
            var tabs = {
                popular: 'Popular',
                favorites: 'Favorites'
            };
            $scope.tabs = tabs;
            $scope.page = 1;
            $scope.shouldHideShots = false;
            
            
            var findAll = function () {
                shotService.listPopular($scope.page, function (res) {
                    $scope.shots = res;
                },
                handleError);
            };

            var findFavorites = function () {
                shotService.listFavorites(function (res) {
                    $scope.favorites = JSON.parse(res);
                },
                handleError);
            };

            var showTab = function (tabName) {
                if (tabName === tabs.popular) {
                    findAll();
                }

                if (tabName === tabs.favorites) {
                    findFavorites();
                }
            };

            $scope.showTab = showTab;

            $scope.addToFavorites = function (item, index) {
                shotService.addToFavorites(item, function () {
                    $scope.shots.splice(index, 1);
                }, handleError)
            };

            $scope.removeFromFavorites = function (id) {
                shotService.removeFromFavorites(id, function () {
                    findFavorites();
                }, handleError)
            };

            $scope.showDetail = function (item) {
                $scope.shouldHideShots = true;
                $scope.shot = item;
            };

            $scope.closeDetail = function () {
                $scope.shouldHideShots = false;
                $scope.shot = {};
            };

            showTab(tabs.popular);
        }
    ]);

    app.filter('htmlToPlaintext', function () {
        return function(text) {
            return String(text).replace(/<[^>]+>/gm, '');
        }
    });

    app.filter('limitTextWidth', function () {
        return function(text) {
            var t = angular.element(text).text(),
                maxLength = 215;
            if (t.length <= maxLength) {
                return t.substring(0, maxLength);
            }
            return t.substring(0, maxLength - 3) + '...';
        }
    });

})(angular);
