var disciplinasController = function($scope, $mdToast, disciplinaApi) {

  $scope.disciplinas = [];

  $scope.listar = function() {
    console.log("Listando")
    disciplinaApi.listar()
      .then(function(response) {
        $scope.disciplinas = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      disciplinaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.disciplinas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.disciplinas = [];
  };

}

app.controller('DisciplinasController', disciplinasController);
