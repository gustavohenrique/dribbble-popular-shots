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
                    scope.showTab(scope.tabs.popular);
                };

                scope.previous = function () {
                    scope.page--;
                    if (scope.page < 1) {
                        scope.page = 1;
                    }
                    scope.showTab(scope.tabs.popular);
                };

            }
        }
    }]);

    app.directive('navItem', ['shotService', function (shotService) {
        return {
            restrict: 'C',
            scope: '&',
            link: function(scope, element, attrs) {
                element.html('<i class="icon ' + attrs.icon + '"></i> ' + attrs.text);

                var menuItems = document.querySelectorAll('a.nav-item');

                var activeCurrentTab = function () {
                    document.querySelector('#' + scope.tabs.popular).classList.add('hide');
                    document.querySelector('#' + scope.tabs.favorites).classList.add('hide');
                    document.querySelector('#' + attrs.text).classList.remove('hide');
                };

                var hidePaginationFor = function (tab) {
                    var pagination = document.querySelector('.nav-pagination');
                    pagination.classList.remove('hide');
                    if (attrs.text === tab) {
                        pagination.classList.add('hide');
                    }
                };

                element.bind('click', function () {

                    for (var i = 0; i < menuItems.length; i++) {
                        menuItems[i].classList.remove('active');
                    }
                    
                    activeCurrentTab();
                    hidePaginationFor(scope.tabs.favorites);

                    element.addClass('active');

                    scope.showTab(attrs.text);
                });
            }
        }
    }]);



})(angular);
