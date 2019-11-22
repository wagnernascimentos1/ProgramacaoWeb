// Endereco - Factory
var enderecoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/enderecos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/enderecos/" + encodeURI(id))
  };

  var _cadastrar = function(endereco) {
    return $http.post(baseUrl + "/endereco", endereco)
  };

  var _atualizar = function(curso) {
    return $http.put(baseUrl+ "/endereco/" + encodeURI(id), endereco)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("enderecoApi", enderecoFactory);
