// Campus - Factory
var campusFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5001";

  var _listar = function() {
    return $http.get(baseUrl+ "/campi")
  };

  var _buscarPorId = function(id) {
    return $http.get(baseUrl+ "/campus/" + encodeURI(id))
  };

  var _cadastrar = function(campus) {
    return $http.post(baseUrl + "/campus", campus)
  };

  var _atualizar = function(campus) {
    return $http.put(baseUrl+ "/campus/" + encodeURI(id), campus)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("campusApi", campusFactory);
