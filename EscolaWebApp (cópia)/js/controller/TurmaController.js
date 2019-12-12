let turmaController = function($scope, turmaApi, $mdToast) {

    $scope.turma = {};

    $scope.cadastrar = function() {

      let turma = angular.copy($scope.turma);


      turmaApi.cadastrar(turma)
      .then(function(response) {
        var toast = $mdToast.simple()
            .textContent('A Turma foi cadastrada com sucesso!')
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
          angular.copy({}, $scope.turma);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.turmaForm.$setPristine();
          $scope.turmaForm.$setUntouched();
          $scope.turmaForm.$setValidity();
      }
}

app.controller("TurmaController", turmaController);
