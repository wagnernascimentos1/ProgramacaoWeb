let escolaController = function($scope, escolaApi, $mdToast) {
    $scope.escola = {};


    $scope.cadastrar = function() {

      let escola = angular.copy($scope.escola);
      escolaApi.cadastrar(escola)
      .then(function(response) {
        var toast = $mdToast.simple()
            .textContent('A Escola foi cadastrado com sucesso!')
            .position('top right')
            .action('OK')
            .hideDelay(6000);
        $mdToast.show(toast);

        limparFormulario();
      })
      .catch(function(error) {
        var toast = $mdToast.simple()
            .textContent('Algum problema ocorreu no envio dos dados.')
            .position('top right')
            .action('OK')
            .hideDelay(6000);
        $mdToast.show(toast);
      });
    }
    let limparFormulario = function () {

          // Reinicializa a variável.
          angular.copy({}, $scope.escola);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.escolaForm.$setPristine();
          $scope.escolaForm.$setUntouched();
          $scope.escolaForm.$setValidity();
      }
}

app.controller("EscolaController", escolaController);
