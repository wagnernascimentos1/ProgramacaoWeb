var campiController = function($scope, $mdToast, campusApi) {

  $scope.campi = [];

  $scope.listar = function() {
      campusApi.listar()
        .then(function(response) {
          $scope.campi = response.data;
        })
        .catch(function(error) {
        });
  };

  $scope.pesquisar = function(sigla) {
    if (sigla.length >= 3) {
      campusApi.buscarPorNome(sigla)
        .then(function(response) {
          $scope.campi = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.sigla = "";
    $scope.campi = [];
  };
}

app.controller('CampiController', campiController);
