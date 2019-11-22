//Aluno.html
var alunoController = function($scope, $mdToast, alunoApi){
  $scope.aluno = {};
  let aluno = $scope.aluno;

  $scope.cadastrar = function(){
    // Converter data do formato brasileiro -> americano
    var data = moment


    alunoApi.cadastrar(aluno)
      .then(function(response) {
        console.log("Requisição enviada e recebida com sucesso.");
        console.log(response);
      })
      .catch(function(error) {
        var toast = $mdToast.simple()
          .textContent('Algum problema ocorreu no envio dos dados.')
          .position('top right')
          .action('OK')
          .hideDelay(6000)
          $mdToast.show(toast);

        });
      }
    }
