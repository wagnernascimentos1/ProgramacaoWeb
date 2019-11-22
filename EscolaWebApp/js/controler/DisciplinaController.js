//disciplina
var disciplinaController = function($scope, $mdToast, disciplinaApi){
  $scope.disciplina = {};
  let disciplina = $scope.disciplina;

  $scope.cadastrar = function(){
    disciplinaApi.cadastrar(disciplina)
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

app.controller('DisciplinaController', disciplinaController);
