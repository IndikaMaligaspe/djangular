(function () {
    'use strict';

    angular
        .module('scrumboard.demo')
        .controller('LoginController', ['$scope', '$location', '$http', LoginController]);

    function LoginController($scope, $location, $http) {
        $scope.login = function () {
            $http.post('/auth_api/login/', $scope.user)
                .then(function () {
                        $location.url('/');
                    },
                    function () {
                        $scope.login_error = "Invalid username/password combination";
                    })
        }

        // activate();

        // function activate() {
        //     if (Login.isLoggedIn()) {
        //         $location.url('/');
        //     }
        // }
    }

})();
