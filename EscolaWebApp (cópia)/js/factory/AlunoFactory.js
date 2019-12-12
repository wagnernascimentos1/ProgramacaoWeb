// Aluno - Factory
var alunoFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5001";

  var _listar = function() {
    return $http.get(baseUrl + "/alunos");
  };

  var _buscarPorId = function(id) {
    return $http.get(baseUrl+ "/alunos/" + encodeURI(id));
  };

  var _cadastrar = function(aluno) {
    return $http.post(baseUrl + "/aluno", aluno);
  };

  var _atualizar = function(aluno) {
    return $http.put(baseUrl+ "/aluno/" + encodeURI(id), aluno);
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("alunoApi", alunoFactory);
