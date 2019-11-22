//turma
var turmaController = function($scope, $mdToast, turmaApi){
  $scope.turma = {};
  let turma = $scope.turma;

  $scope.cadastrar = function(){
    turmaApi.cadastrar(turma)
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

app.controller('TurmaController', turmaController);
