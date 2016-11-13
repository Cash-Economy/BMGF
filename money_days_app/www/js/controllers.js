angular.module('app.controllers', [])

.controller('savePageCtrl', ['$rootScope', '$scope', '$stateParams', '$http',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams, $http) {

    $rootScope.moneydaysURL = 'http://10.128.19.187:8000';
    $scope.totalSaved = 550;
    $scope.goal = 2500;
    $scope.progressToGoal = parseInt($scope.totalSaved/$scope.goal*100);

    $scope.balanceInAccount = 400;
    $rootScope.userID = 1;
    $http({
      method:'GET',
      url: $scope.moneydaysURL + '/api/users/' + $scope.userID.toString,
      headers : {
        'Content-Type' : 'application/json',
        'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
      }
    }).then(function successCallback(response) {
      console.log(response);
    },
    function errorCallback(response){
      // offline alert - can't save money
      console.log(response);
    })

    $scope.coachTips = [
        "Post1.jpg", "Post2.jpg", "Post3.jpg"
    ];

    $rootScope.saveRecommended = 50;
    $rootScope.saveAmount = 50;

    $rootScope.save = function() {
      if($scope.saveAmount < $scope.balanceInAccount){
        console.log("Saved Amount", $scope.saveAmount);
        $scope.totalSaved += $scope.saveAmount;
        $scope.progressToGoal = parseInt($scope.totalSaved/$scope.goal*100);
        $scope.balanceInAccount -= $scope.saveAmount;
        // goaal reached ! - color red !, new badge
        //
        $http({
          method: 'POST',
          url: $scope.moneydaysURL + '/api/users/1/contributions/',
          headers : {
            'Content-Type' : 'application/json',
            'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
          },
          data: {txn_amount: $scope.saveAmount}
        }).then(function successCallback(response) {
            console.log("Saved successfully" + response);
        }, function errorCallback(response) {
            console.log("Error in saving" + response);
        });
      }
      else
        console.log("No balance in account");
    };

    $rootScope.less = function() {
      if($scope.saveAmount>10)
        $scope.saveAmount -= 10;
    };

    $rootScope.more = function() {
      if($scope.saveAmount <= 0.4*$scope.balanceInAccount)
        $scope.saveAmount += 10;
      else
        console.log("Greater than 40% of Balance in your Account");
    };

}])

.controller('lotteryPageCtrl', ['$rootScope', '$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams) {
  $scope.totalPoints = 250;
  $scope.saveAmount = $rootScope.saveAmount;

}])

.controller('socialPageCtrl', ['$rootScope', '$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams) {
  $scope.saveAmount = $rootScope.saveAmount;

}])

.controller('menuCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])

.controller('withdrawPageCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])

.controller('shopCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])

.controller('settingsCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
