var turmasController = function($scope, $mdToast, turmaApi) {

  $scope.turmas = [];

  $scope.listar = function() {
    console.log("Listando")
    turmaApi.listar()
      .then(function(response) {
        $scope.turmas = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      turmaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.turmas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.turmas = [];
  };

}

app.controller('TurmasController', turmasController);
