angular.module('myApp').controller('MyCtrl',['$scope','$http',function($scope,$http) {

var data = {
    first_name: 'sivan',
    last_name:'das',
    email:'sivan@gmail.com'
};
   
  var url="http://127.0.0.1:8000/author/";
    $http.post(url,data).success( function(response){
      $scope.post = response;

    });

}]);
