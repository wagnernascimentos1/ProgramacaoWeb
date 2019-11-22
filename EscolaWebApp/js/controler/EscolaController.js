//escola
var escolaController = function($scope, $mdToast, escolaApi){
  $scope.escola = {};
  let escola = $scope.escola;

  $scope.cadastrar = function(){
    escolaApi.cadastrar(escola)
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

app.controller('EscolaController', escolaController);
