/** @odoo-module **/ 
import { registry } from "@web/core/registry"; 
import { kanbanView } from "@web/views/kanban/kanban_view"; 
import { KanbanController } from "@web/views/kanban/kanban_controller"; 
import { useService } from "@web/core/utils/hooks"; 


// const { onWillStart } = owl;


class DocumentosKanbanController extends KanbanController { 
    setup() { 
        super.setup(); 
        console.log("quetzal"); 
        // this.orm = useService("orm"); 
     

        // onWillStart(async ()=>{ 
        //     const documentos = await this.orm.searchRead("documentos.documentos", ["folder_id"]); 
        // console.log(documentos); 
        // })
    }
} 

// DocumentosKanbanController.template = "owl.DocumentosKanbanView"; 

export const documentosKanbanView = { 
    ...kanbanView, 
    Controller: DocumentosKanbanController, 
}; 

registry.category("views").add("documentos_kanban_view", documentosKanbanView);
