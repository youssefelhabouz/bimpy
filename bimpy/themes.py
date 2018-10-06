import bimpy

def set_light_theme():
    """ light style from Pacome Danhiez (user itamago) https://github.com/ocornut/imgui/pull/511#issuecomment-175719267 """

    style = bimpy.get_style()
    style.set_color(bimpy.Colors.Text, bimpy.Vec4(0.00, 0.00, 0.00, 1.00))
    style.set_color(bimpy.Colors.TextDisabled, bimpy.Vec4(0.60, 0.60, 0.60, 1.00))
    style.set_color(bimpy.Colors.WindowBg, bimpy.Vec4(0.94, 0.94, 0.94, 1.00))
    style.set_color(bimpy.Colors.ChildWindowBg, bimpy.Vec4(0.00, 0.00, 0.00, 0.00))
    style.set_color(bimpy.Colors.Border, bimpy.Vec4(0.00, 0.00, 0.00, 0.39))
    style.set_color(bimpy.Colors.BorderShadow, bimpy.Vec4(1.00, 1.00, 1.00, 0.10))
    style.set_color(bimpy.Colors.FrameBg, bimpy.Vec4(1.00, 1.00, 1.00, 1.00))
    style.set_color(bimpy.Colors.FrameBgHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(bimpy.Colors.FrameBgActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(bimpy.Colors.TitleBg, bimpy.Vec4(0.96, 0.96, 0.96, 1.00))
    style.set_color(bimpy.Colors.TitleBgCollapsed, bimpy.Vec4(1.00, 1.00, 1.00, 0.51))
    style.set_color(bimpy.Colors.TitleBgActive, bimpy.Vec4(0.82, 0.82, 0.82, 1.00))
    style.set_color(bimpy.Colors.MenuBarBg, bimpy.Vec4(0.86, 0.86, 0.86, 1.00))
    style.set_color(bimpy.Colors.ScrollbarBg, bimpy.Vec4(0.98, 0.98, 0.98, 0.53))
    style.set_color(bimpy.Colors.ScrollbarGrab, bimpy.Vec4(0.69, 0.69, 0.69, 0.80))
    style.set_color(bimpy.Colors.ScrollbarGrabHovered, bimpy.Vec4(0.49, 0.49, 0.49, 0.80))
    style.set_color(bimpy.Colors.ScrollbarGrabActive, bimpy.Vec4(0.49, 0.49, 0.49, 1.00))
    # style.set_color(bimpy.Colors.ComboBg, bimpy.Vec4(0.86, 0.86, 0.86, 0.99))
    style.set_color(bimpy.Colors.CheckMark, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.SliderGrab, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(bimpy.Colors.SliderGrabActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.Button, bimpy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(bimpy.Colors.ButtonHovered, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.ButtonActive, bimpy.Vec4(0.06, 0.53, 0.98, 1.00))
    style.set_color(bimpy.Colors.Header, bimpy.Vec4(0.26, 0.59, 0.98, 0.31))
    style.set_color(bimpy.Colors.HeaderHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.80))
    style.set_color(bimpy.Colors.HeaderActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.Column, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(bimpy.Colors.ColumnHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(bimpy.Colors.ColumnActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.ResizeGrip, bimpy.Vec4(0.50, 0.50, 0.50, 1.00))
    style.set_color(bimpy.Colors.ResizeGripHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(bimpy.Colors.ResizeGripActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.95))
    # style.set_color(bimpy.Colors.CloseButton, bimpy.Vec4(0.59, 0.59, 0.59, 0.50))
    # style.set_color(bimpy.Colors.CloseButtonHovered, bimpy.Vec4(0.98, 0.39, 0.36, 1.00))
    # style.set_color(bimpy.Colors.CloseButtonActive, bimpy.Vec4(0.98, 0.39, 0.36, 1.00))
    style.set_color(bimpy.Colors.PlotLines, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(bimpy.Colors.PlotLinesHovered, bimpy.Vec4(1.00, 0.43, 0.35, 1.00))
    style.set_color(bimpy.Colors.PlotHistogram, bimpy.Vec4(0.90, 0.70, 0.00, 1.00))
    style.set_color(bimpy.Colors.PlotHistogramHovered, bimpy.Vec4(1.00, 0.60, 0.00, 1.00))
    style.set_color(bimpy.Colors.TextSelectedBg, bimpy.Vec4(0.26, 0.59, 0.98, 0.35))
    style.set_color(bimpy.Colors.PopupBg, bimpy.Vec4(1.00, 1.00, 1.00, 0.94))
    style.set_color(bimpy.Colors.ModalWindowDarkening, bimpy.Vec4(0.20, 0.20, 0.20, 0.35))
    bimpy.set_style(style)
