let disciplinaController = function($scope, disciplinaApi, $mdToast){

    $scope.nome = {};

    $scope.cadastrar = function() {

      let disciplina = angular.copy($scope.disciplina);






      disciplinaApi.cadastrar(disciplina)
      .then(function(response) {
        var toast = $mdToast.simple()
            .textContent('A Disciplina foi cadastrado com sucesso!')
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
          angular.copy({}, $scope.disciplina);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.disciplinaForm.$setPristine();
          $scope.disciplinaForm.$setUntouched();
          $scope.disciplinaForm.$setValidity();
      }
}

app.controller("DisciplinaController", disciplinaController);
