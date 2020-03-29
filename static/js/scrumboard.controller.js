(function(){
    'use strict';
    angular.module('scrumboard.demo', ['ngRoute'])
    .controller('ScrumboardController', ['$scope', '$http', 'Login',  ScrumboardController]);

    function ScrumboardController($scope, $http, Login){
        $scope.add = function(list, title){
          var card = {
              list: list.id,
              title: title
          };
          $http.post('/scrumboard/cards/',card).then(
              function(response){
                list.cards.push(card);
              },
              function(){
                alert('Could not create card');
              });
          
        };

        Login.redirectIfNotLoggedIn();
        $scope.data = [];
        $scope.logout = Login.logout;

        $http.get('http://127.0.0.1:8000/scrumboard/lists').then(function(response){
            $scope.data = response.data;
        });
        
    }
}());