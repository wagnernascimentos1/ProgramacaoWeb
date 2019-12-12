let turnoController = function($scope, turnoApi, $mdToast) {

    $scope.turno = {};

    $scope.cadastrar = function() {

      let turno = angular.copy($scope.turno);

      turnoApi.cadastrar(turno)
      .then(function(response) {
        var toast = $mdToast.simple()
            .textContent('O Turno foi cadastrado com sucesso!')
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
          angular.copy({}, $scope.turno);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.turnoForm.$setPristine();
          $scope.turnoForm.$setUntouched();
          $scope.turnoForm.$setValidity();
      }
}

app.controller("TurnoController", turnoController);
