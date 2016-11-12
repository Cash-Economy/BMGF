angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('tabsController.savePage', {
    url: '/savepage',
    views: {
      'tab1': {
        templateUrl: 'templates/savePage.html',
        controller: 'savePageCtrl'
      }
    }
  })

  .state('tabsController.lotteryPage', {
    url: '/lotterypage',
    views: {
      'tab2': {
        templateUrl: 'templates/lotteryPage.html',
        controller: 'lotteryPageCtrl'
      }
    }
  })

  .state('tabsController.socialPage', {
    url: '/socialpage',
    views: {
      'tab3': {
        templateUrl: 'templates/socialPage.html',
        controller: 'socialPageCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/page1',
    templateUrl: 'templates/tabsController.html',
    abstract:true
  })

  .state('withdrawPage', {
    url: '/withdraw',
    templateUrl: 'templates/withdrawPage.html',
    controller: 'withdrawPageCtrl'
  })

  .state('shop', {
    url: '/shop',
    templateUrl: 'templates/shop.html',
    controller: 'shopCtrl'
  })

  .state('settings', {
    url: '/settings',
    templateUrl: 'templates/settings.html',
    controller: 'settingsCtrl'
  })

$urlRouterProvider.otherwise('/page1/savepage')

  

});