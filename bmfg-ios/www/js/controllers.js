angular.module('app.controllers', [])

.controller('savePageCtrl', ['$rootScope', '$scope', '$stateParams', '$http',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams, $http) {

    $rootScope.moneydaysURL = 'http://10.128.19.187:8000';
    //$rootScope.totalSaved = 550;
    //$rootScope.goal = 2500;
    //$rootScope.progressToGoal = parseInt($rootScope.totalSaved/$rootScope.goal*100);

    //$rootScope.balanceInAccount = 400;
    //$rootScope.saveRecommended = 50;
    //$rootScope.saveAmount = 50;

    $rootScope.userID = 1;

    $scope.getUpdates = function() {
      $http({
        method: 'GET',
        url: $rootScope.moneydaysURL + '/api/users/1/contributions/',
        headers : {
          'Content-Type' : 'application/json',
          'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
        }
      }).then(function successCallback(response) {
          $rootScope.totalSaved = parseFloat(response.data.results[0].balance).toFixed(2);
          console.log("Balance " + parseFloat(response.data.results[0].balance).toFixed(2));
        }, function errorCallback(response) {
          console.log("Error ");
          console.log(response);
        });

        $http({
          method:'GET',
          url: $rootScope.moneydaysURL + '/api/users/1',
          headers : {
            'Content-Type' : 'application/json',
            'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
          }
        }).then(function successCallback(response) {
          console.log(response.data.recommended_amount);
          $rootScope.saveRecommended = response.data.recommended_amount;
          $rootScope.saveAmount = $rootScope.saveRecommended;
    //       {
    //     "url": "http://10.128.19.187:8000/api/users/1/",
    //     "id": 1,
    //     "email": "mr2224@cornell.edu",
    //     "first_name": "Mario",
    //     "last_name": "Rial Amado",
    //     "gender": "F",
    //     "birth_day": "1992-01-14",
    //     "checking_account_id": "5827fa44360f81f10454a860",
    //     "recommended_amount": 0,
    //     "coach_tip": null
    // }
        },
        function errorCallback(response){
          // offline alert - can't save money
          console.log(response);
        });

        $http({
          method: 'GET',
          url: $rootScope.moneydaysURL + '/api/users/1/goals',
          headers : {
            'Content-Type' : 'application/json',
            'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
          }
        }).then(function successCallback(response){
          $rootScope.goal = response.data.results[0].amount;
          $rootScope.progressToGoal = parseInt($rootScope.totalSaved/$rootScope.goal*100);
        },
        function errorCallback(response){
          console.log(response);
        })
    };

    $scope.getUpdates();

    $rootScope.coachTips = [
        "Post1.jpg", "Post2.jpg", "Post3.jpg"
    ];

    $rootScope.save = function() {
        $http({
          method: 'POST',
          url: $rootScope.moneydaysURL + '/api/users/1/contributions/',
          headers : {
            'Content-Type' : 'application/json',
            'Authorization': 'Basic bXIyMjI0QGNvcm5lbGwuZWR1OnJvYmxlMTQwMTky'
          },
          data: {txn_amount: $rootScope.saveAmount}
        }).then(function successCallback(response) {
            console.log("Saved successfully" + response);
            $scope.getUpdates();
            //
            //$rootScope.totalSaved += $rootScope.saveAmount;
            $rootScope.progressToGoal = parseInt($rootScope.totalSaved/$rootScope.goal*100);
            //$rootScope.balanceInAccount -= parseFloat($rootScope.saveAmount).toFixed(2);
            //$rootScope.saveAmount = parseFloat($rootScope.saveRecommended).toFixed(2);
            // goaal reached ! - color red !, new badge
            //
        }, function errorCallback(response) {
            console.log("Error in saving" + response);
        });
      };

    $rootScope.less = function() {
      if($rootScope.saveAmount>10)
        $rootScope.saveAmount -= 10;
    };

    $rootScope.more = function() {
        $rootScope.saveAmount += 10;
    };

    $rootScope.totalPoints = 250;
}])

.controller('lotteryPageCtrl', ['$rootScope', '$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams) {

  $rootScope.saveAmount = $rootScope.saveAmount;

}])

.controller('socialPageCtrl', ['$rootScope', '$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($rootScope, $scope, $stateParams) {
  $rootScope.saveAmount = $rootScope.saveAmount;

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
