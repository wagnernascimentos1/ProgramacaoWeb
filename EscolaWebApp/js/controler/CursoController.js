//curso
var cursoController = function($scope, $mdToast, cursoApi){
  $scope.curso = {};
  let curso = $scope.curso;

  $scope.cadastrar = function(){
    cursoApi.cadastrar(curso)
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

app.controller('CursoController', cursoController);
