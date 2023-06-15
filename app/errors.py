erros = {"status_code": {
    404: {"description": "Not Found",
          "content": {"application/json": {"example": {
              "detail": "Não encontrado"}}}},
    409: {"description": "Duplicado",
          "content": {"application/json": {"example": {
              "detail": "Duplicado"}}}}}}
