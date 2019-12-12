let enderecoController = function($scope, enderecoApi, $mdToast) {

    $scope.endereco = {};

    $scope.cadastrar = function() {

      let endereco = angular.copy($scope.endereco);

      enderecoApi.cadastrar(endereco)
      .then(function(response) {
        var toast = $mdToast.simple()
            .textContent('O Endereço foi cadastrado com sucesso!')
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
          angular.copy({}, $scope.endereco);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.enderecoForm.$setPristine();
          $scope.enderecoForm.$setUntouched();
          $scope.enderecoForm.$setValidity();
      }
}

app.controller("EnderecoController", enderecoController);
