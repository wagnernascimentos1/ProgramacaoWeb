var escolasController = function($scope, $mdToast, escolaApi) {

  $scope.escolas = [];

  $scope.listar = function() {
    console.log("Listando")
    escolaApi.listar()
      .then(function(response) {
        $scope.escolas = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      escolaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.escolas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.escolas = [];
  };

}

app.controller('EscolasController', escolasController);
