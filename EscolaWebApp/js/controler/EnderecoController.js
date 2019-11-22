//endereço
var endereçoController = function($scope, $mdToast, endereçoApi){
  $scope.endereço = {};
  let campus = $scope.endereço;

  $scope.cadastrar = function(){
    endereçoApi.cadastrar(endereço)
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

app.controller('EndereçoController', endereçoController);
