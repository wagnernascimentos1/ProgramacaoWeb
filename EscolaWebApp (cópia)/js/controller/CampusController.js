var campusController = function($scope, $mdToast, $state, campusApi) {

  $scope.campus = {};

  $scope.cadastrar = function() {
    // Criar uma cópia do aluno do $scope.
    let campus = angular.copy($scope.campus);


    campusApi.cadastrar(campus)
      .then(function(response) {

        // Limpar formulário.
        limparFormulario();

        // Redirecionamento de página.
        $state.transitionTo('campi', {reload: true, inherit: false, notify: true});

        // Caixa de confirmação - Toast
        var toast = $mdToast.simple()
          .textContent('O campus foi cadastrado com sucesso!')
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);
      })
      .catch(function(error) {
        var toast = $mdToast.simple()
          .textContent('Algum problema ocorreu no envio dos dados.')
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);
      });
  };

  let limparFormulario = function() {

    // Reinicializa a variável aluno.
    angular.copy({}, $scope.campus);

    // Reinicializa o estado do campo para os eventos e validação.
    // É necessário indicar o atributo name no formulário <form>
    $scope.campusForm.$setPristine();
    $scope.campusForm.$setUntouched();
    $scope.campusForm.$setValidity();
  }
}

app.controller('CampusController', campusController);
