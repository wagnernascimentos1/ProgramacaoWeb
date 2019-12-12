// Disciplina - Factory
var disciplinaFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5001";

  var _listar = function() {
    return $http.get(baseUrl+ "/disciplinas")
  };

  var _buscarPorId = function(id) {
    return $http.get(baseUrl+ "/disciplinas/" + encodeURI(id))
  };

  var _cadastrar = function(disciplina) {
    return $http.post(baseUrl + "/disciplina", disciplina)
  };

  var _atualizar = function(disciplina) {
    return $http.put(baseUrl+ "/disciplina/" + encodeURI(id), disciplina)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("disciplinaApi", disciplinaFactory);
