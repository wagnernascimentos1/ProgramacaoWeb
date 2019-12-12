let homeController = function($scope){
  $scope.logradouro = "Outro Valor";

  $scope.numero1 = 0;
  $scope.numero2 = 0;

  $scope.somar = function(numero1, numero2){
    $scope.resultado = numero1 + numero2 ;
  }

  function somar(numero1, numero2){
    return numero1 + numero2;
  }
}

app.controller('HomeController', homeController);
