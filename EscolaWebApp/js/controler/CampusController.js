//campus
var campusController = function($scope, $mdToast, campusApi){
  $scope.campus = {};
  let campus = $scope.campus;

  $scope.cadastrar = function(){
    campusApi.cadastrar(campus)
    .then(function(response) {
      console.log("Requisição enviada e recebida com sucesso!");
      console.log(response);
    })
    .catch(function(error) {
      var toast = $mdToast.simple()
        .textContent('Algum problema ocorreu no envio dos dados :c tururuuu...')
        .position('top right')
        .action('OK')
        .hideDelay(6000);
      $mdToast.show(toast);
    });
  }
}

app.controller('CampusController', campusController);
