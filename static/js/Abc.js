angular.module('myApp').controller('Abc',['$scope','$http',function($scope,$http) {

$scope.add = function() {
	
        data= {
	first_name : $scope.firstname,
	last_name:$scope.lastname,
	email:$scope.email
};
   var url="http://127.0.0.1:8000/author/";
    $http.post(url,data).success( function(response){
      $scope.hello = response;

    });
}

}]);
