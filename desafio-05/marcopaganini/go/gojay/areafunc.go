// Implementa o parser de áreas ou funcionários.
package main

import (
	"github.com/francoispqt/gojay"
)

// areaOrFunc parsa o header json inicial de área ou funcionário.
type areaOrFunc struct {
	funcs *funcList
	areas *areasList
}

// Implement UnmarshalerJSONObject
func (x *areaOrFunc) UnmarshalJSONObject(dec *gojay.Decoder, k string) error {
	switch k {
	case "funcionarios":
		return dec.Array(x.funcs)
	case "areas":
		return dec.Array(x.areas)
	}
	return nil
}

func (x *areaOrFunc) NKeys() int {
	return 0
}
