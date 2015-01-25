(function (angular) {
    'use strict';

    var app = angular.module('ShotController', ['ShotService']);

    app.controller('ShotCtrl', ['$scope', 'shotService',

        function ($scope, shotService) {

            var handleError = function (res) {};
            
            $scope.page = 1;
            $scope.shouldHideShots = false;
            
            
            $scope.findAll = function () {
                shotService.listPopular($scope.page, function (res) {
                    $scope.shots = res;
                    console.log(res[0]);
                },
                handleError);
            };

            $scope.findAll();

            $scope.showDetail = function (item) {
                $scope.shouldHideShots = true;
                $scope.shot = item;
            };

            $scope.closeDetail = function () {
                $scope.shouldHideShots = false;
                $scope.shot = {};
            };
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
