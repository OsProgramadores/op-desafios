// Implementação do parser de áreas
package main

import (
	"github.com/francoispqt/gojay"
)

// areasType guarda informações sobre as áreas.
type areasRecord struct {
	codigo string
	nome   string
}

// Implementa UnmarshalerJSONObject.
func (x *areasRecord) UnmarshalJSONObject(dec *gojay.Decoder, k string) error {
	switch k {
	case "codigo":
		return dec.String(&x.codigo)
	case "nome":
		return dec.String(&x.nome)
	}
	return nil
}

func (x *areasRecord) NKeys() int {
	return 0
}

// areasList decodifica a lista de áreas.
type areasList struct {
	aRecord          *areasRecord
	areasCodeAndName map[string]string
}

// Implementa UnmarshalerJSONObject em areasList.
func (x *areasList) UnmarshalJSONArray(dec *gojay.Decoder) error {
	// Decodifica os dados de uma área no array JSON.
	if err := dec.Object(x.aRecord); err != nil {
		return err
	}
	x.areasCodeAndName[x.aRecord.codigo] = x.aRecord.nome
	return nil
}
