// Escola - Factory
var escolaFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/escolas")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/escolas/" + encodeURI(id))
  };

  var _cadastrar = function(escola) {
    return $http.post(baseUrl + "/escola", escola)
  };

  var _atualizar = function(escola) {
    return $http.put(baseUrl+ "/escola/" + encodeURI(id), escola)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("escolaApi", escolaFactory);
