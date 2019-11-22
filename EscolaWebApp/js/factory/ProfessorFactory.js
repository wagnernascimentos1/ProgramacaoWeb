// Professor - Factory
var professorFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/professores")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/professores/" + encodeURI(id))
  };

  var _cadastrar = function(professor) {
    return $http.post(baseUrl + "/professor", professor)
  };

  var _atualizar = function(professor) {
    return $http.put(baseUrl+ "/professor/" + encodeURI(id), professor)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("professorApi", professorFactory);
