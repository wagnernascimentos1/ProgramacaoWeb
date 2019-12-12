var enderecosController = function($scope, $mdToast, enderecoApi) {

  $scope.enderecos = [];

  $scope.listar = function() {
    console.log("Listando")
    enderecoApi.listar()
      .then(function(response) {
        $scope.enderecos = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(logradouro) {
    if (logradouro.length >= 3) {
      enderecoApi.buscarPorNome(logradouro)
        .then(function(response) {
          $scope.enderecos = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.logradouro = "";
    $scope.enderecos = [];
  };

}

app.controller('EnderecosController', enderecosController);
