var professoresController = function($scope, $mdToast, professorApi) {

  $scope.professores = [];

  $scope.listar = function() {
    console.log("Listando")
    professorApi.listar()
      .then(function(response) {
        $scope.professores = response.data;
      })
      .catch(function(error) {

      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      professorApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.professores = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.limparBusca = function() {
    $scope.nome = "";
    $scope.professores = [];
  };

}

app.controller('ProfessoresController', professoresController);
