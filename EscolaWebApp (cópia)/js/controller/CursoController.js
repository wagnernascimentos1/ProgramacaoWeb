//curso
let cursoController = function($scope, cursoApi, $mdToast) {

    $scope.curso = {}

    $scope.cadastrar = function() {

      let curso = angular.copy($scope.curso);






      cursoApi.cadastrar(curso)
        .then(function(response) {
          var toast = $mdToast.simple()
              .textContent('O Curso foi cadastrado com sucesso!')
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

          // Reinicializa a variável
          angular.copy({}, $scope.curso);

          // Reinicializa o estado do campo para os eventos e validação.
          // É necessário indicar o atributo name no formulário <form>
          $scope.cursoForm.$setPristine();
          $scope.cursoForm.$setUntouched();
          $scope.cursoForm.$setValidity();
      }
}

app.controller("CursoController", cursoController);
