(function (angular) {
    'use strict';

    var app = angular.module('ShotDirectives', ['ShotService']);

    app.directive('pagination', ['shotService', function (shotService) {
        return {
            restrict: 'A',
            template: '<a class="item" ng-click="previous()"><i class="left arrow icon"></i> Previous</a> \
            <a class="item">{{ page }}</a> \
            <a class="item" ng-click="next()">Next <i class="right arrow icon""></i></a>',
            scope: '=',
            link: function(scope, element, attrs) {
                scope.next = function () {
                    scope.page++;
                    scope.findAll();
                };

                scope.previous = function () {
                    scope.page--;
                    if (scope.page < 1) {
                        scope.page = 1;
                    }
                    scope.findAll();
                };

            }
        }
    }]);



})(angular);
