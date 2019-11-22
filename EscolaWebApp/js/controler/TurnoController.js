//turno
var turnoController = function($scope, $mdToast, turnoApi){
  $scope.turno = {};
  let turno = $scope.turno;

  $scope.cadastrar = function(){
    turnoApi.cadastrar(turno)
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

app.controller('TurnoController', turnoController);
