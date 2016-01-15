angular.module('myApp').controller('student2Controller',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/author/";
    $http.get(url).success( function(response){
      $scope.students2 = response;

    });

}]);
