Ext.define('MainHub.store.tables.libraries.NucleicAcidTypes', {
    extend: 'Ext.data.Store',
    storeId: 'nucleicAcidTypesStore',

    requires: [
        'MainHub.model.tables.libraries.SampleNucleicAcidType'
    ],

    model: 'MainHub.model.tables.libraries.SampleNucleicAcidType',

    proxy: {
        type: 'ajax',
        url: 'get_nucleic_acid_types/',
        timeout: 1000000,
        pageParam: false,   //to remove param "page"
        startParam: false,  //to remove param "start"
        limitParam: false,  //to remove param "limit"
        noCache: false,     //to remove param "_dc",
        reader: {
            type: 'json',
            rootProperty: 'data',
            successProperty: 'success'
        }
    },

    listeners: {
        load: function(store, records, success, operation) {
            if (!success) {
                var response = operation._response,
                    obj = Ext.JSON.decode(response.responseText);
                console.log('[ERROR]: get_nucleic_acid_types(): ' + obj.error);
                console.log(response);
            }
        }
    }
});
