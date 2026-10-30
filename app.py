bl_info = {
    "name": "Mi Menú Lateral Profesional",
    "author": "Tu Nombre",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Mi Menú",
    "description": "Ejemplo básico de creación de un panel lateral con la API de Python",
    "category": "Development",
}

import bpy

class VIEW3D_PT_CustomSidebarPanel(bpy.types.Panel):
    """Crea un Panel Personalizado en la barra lateral del 3D Viewport"""
    bl_label = "Menú Principal 2"          # Título que aparece en la cabecera del panel
    bl_idname = "VIEW3D_PT_custom_sidebar" # ID único del panel
    bl_space_type = 'VIEW_3D'            # Área de Blender donde se mostrará (Vista 3D)
    bl_region_type = 'UI'              # Región de la interfaz (UI corresponde a la barra lateral / N-Panel)
    bl_category = 'Mi Menú'              # Nombre de la pestaña en la barra lateral

    def draw(self, context):
        layout = self.layout

        # Fila con una etiqueta informativa
        row = layout.row()
        row.label(text="Herramientas de Modelado", icon='MESH_DATA')

        # Fila con un botón operador nativo de Blender (ej: Crear Cubo)
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Crear Cubo", icon='MESH_CUBE')

        # Fila con un botón operador para el plano
        row = layout.row()
        row.operator("mesh.primitive_plane_add", text="Crear Plano", icon='MESH_PLANE')

        # Separador visual
        layout.separator()

        # Sección con diseño en columna
        col = layout.column(align=True)
        col.label(text="Opciones Avanzadas:")
        col.operator("object.shade_smooth", text="Suavizar Sombras")
        col.operator("object.shade_flat", text="Caras Planas")

# Clases a registrar y desregistrar
classes = (
    VIEW3D_PT_CustomSidebarPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()